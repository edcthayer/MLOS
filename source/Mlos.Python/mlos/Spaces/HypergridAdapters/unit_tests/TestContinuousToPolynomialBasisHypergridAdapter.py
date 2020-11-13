#
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
#
import math
import numpy as np
from mlos.Spaces import SimpleHypergrid, CategoricalDimension, ContinuousDimension, DiscreteDimension, OrdinalDimension
from mlos.OptimizerEvaluationTools.SyntheticFunctions.ThreeLevelQuadratic import ThreeLevelQuadratic
from mlos.Spaces.HypergridAdapters import ContinuousToPolynomialBasisHypergridAdapter


class TestContinuousToPolynomialBasisHypergridAdapter:

    @classmethod
    def setup_class(cls) -> None:

        cls.simple_hypergrid = SimpleHypergrid(
            name='simple_adaptee',
            dimensions=[
                CategoricalDimension(name='categorical_mixed_types', values=['red', True, False, 5]),
                DiscreteDimension(name='one_to_ten', min=1, max=10),
                ContinuousDimension(name='z_one', min=-1, max=2),
                ContinuousDimension(name='z_two', min=-2, max=1),
                ContinuousDimension(name='z_3', min=-2, max=-1),
                OrdinalDimension(name='ordinal_mixed_types', ordered_values=[1, False, 'two'])
            ]
        )

        cls.unbalanced_hierarchical_hypergrid = SimpleHypergrid(
            name='hierarchical_adaptee',
            dimensions=[
                CategoricalDimension(name='categorical_mixed_types', values=['red', True, False, 3]),
                DiscreteDimension(name='one_to_ten', min=1, max=10),
                ContinuousDimension(name='x1', min=-1, max=1),
                ContinuousDimension(name='x2', min=-1, max=1),
                OrdinalDimension(name='ordinal_mixed_types', ordered_values=[3, False, 'two'])
            ]
        ).join(
            subgrid=SimpleHypergrid(
                name="nested_grid",
                dimensions=[
                    CategoricalDimension(name='categorical_mixed_types', values=['red', False, True, 3]),
                    DiscreteDimension(name='one_to_ten', min=1, max=10),
                    ContinuousDimension(name='x1', min=-1, max=1),
                    ContinuousDimension(name='x2', min=-1, max=1),
                    OrdinalDimension(name='ordinal_mixed_types', ordered_values=[3, 'two', False])
                ]
            ),
            on_external_dimension=CategoricalDimension("categorical_mixed_types", values=[True])
        )

        cls.balanced_hierarchical_hypergrid = ThreeLevelQuadratic().parameter_space

    @staticmethod
    def n_choose_k(n, k):
        return math.factorial(n) / math.factorial(k) / math.factorial(n - k)

    ## simple_hypergrid tests
    # dataframe projections
    def test_simple_hypergrid_degree_two_all_terms_dataframe(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': False}
        self._test_dataframe_projection(adaptee=self.simple_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_simple_hypergrid_degree_three_all_terms_dataframe(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': False}
        self._test_dataframe_projection(adaptee=self.simple_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_simple_hypergrid_degree_two_no_interaction_terms_dataframe(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': True}
        self._test_dataframe_projection(adaptee=self.simple_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_simple_hypergrid_degree_three_no_interaction_terms_dataframe(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': True}
        self._test_dataframe_projection(adaptee=self.simple_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    # point projections
    def test_simple_hypergrid_degree_two_all_terms_point(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': False}
        self._test_point_projection(adaptee=self.simple_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_simple_hypergrid_degree_three_all_terms_point(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': False}
        self._test_point_projection(adaptee=self.simple_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_simple_hypergrid_degree_two_interactions_only_terms_point(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': True}
        self._test_point_projection(adaptee=self.simple_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_simple_hypergrid_degree_three_interactions_only_terms_point(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': True}
        self._test_point_projection(adaptee=self.simple_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    ## unbalanced_hierarchical_hypergrid tests
    # dataframe projection tests
    def test_unbalanced_hierarchical_hypergrid_degree_two_all_terms_dataframe(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': False}
        self._test_dataframe_projection(adaptee=self.unbalanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_unbalanced_hierarchical_hypergrid_degree_three_all_terms_dataframe(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': False}
        self._test_dataframe_projection(adaptee=self.unbalanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_unbalanced_hierarchical_hypergrid_degree_two_interactions_only_dataframe(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': True}
        self._test_dataframe_projection(adaptee=self.unbalanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_unbalanced_hierarchical_hypergrid_degree_three_interactions_only_dataframe(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': True}
        self._test_dataframe_projection(adaptee=self.unbalanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    # point projection tests
    def test_unbalanced_hierarchical_hypergrid_degree_two_all_terms_point(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': False}
        self._test_point_projection(adaptee=self.unbalanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_unbalanced_hierarchical_hypergrid_degree_three_all_terms_point(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': False}
        self._test_point_projection(adaptee=self.unbalanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_unbalanced_hierarchical_hypergrid_degree_two_interactions_only_point(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': True}
        self._test_point_projection(adaptee=self.unbalanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_unbalanced_hierarchical_hypergrid_degree_three_interactions_only_point(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': True}
        self._test_point_projection(adaptee=self.unbalanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    ## balanced_hierarchical_hypergrid_tests
    # dataframe projection tests
    def test_balanced_hierarchical_hypergrid_degree_two_all_terms_dataframe(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': False}
        self._test_dataframe_projection(adaptee=self.balanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_balanced_hierarchical_hypergrid_degree_three_all_terms_dataframe(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': False}
        self._test_dataframe_projection(adaptee=self.balanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_balanced_hierarchical_hypergrid_degree_two_interactions_only_dataframe(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': True}
        self._test_dataframe_projection(adaptee=self.balanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_balanced_hierarchical_hypergrid_degree_three_interactions_only_dataframe(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': True}
        self._test_dataframe_projection(adaptee=self.balanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    # point projection tests
    def test_balanced_hierarchical_hypergrid_degree_two_all_terms_point(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': False}
        self._test_point_projection(adaptee=self.balanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_balanced_hierarchical_hypergrid_degree_three_all_terms_point(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': False}
        self._test_point_projection(adaptee=self.balanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_balanced_hierarchical_hypergrid_degree_two_interactions_only_point(self):
        adapter_kwargs = {'degree': 2, 'interaction_only': True}
        self._test_point_projection(adaptee=self.balanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    def test_balanced_hierarchical_hypergrid_degree_three_interactions_only_point(self):
        adapter_kwargs = {'degree': 3, 'interaction_only': True}
        self._test_point_projection(adaptee=self.balanced_hierarchical_hypergrid, adapter_kwargs=adapter_kwargs, num_random_points=10)

    # @pytest.mark.parametrize("degree", [2, 11])
    # @pytest.mark.parametrize("interaction_only", [True, False])
    # @pytest.mark.parmaetrize("adaptee", [self.simple_hypergrid, self.unbalanced_hierarchical_hypergrid, self.balanced_hierarchical_hypergrid])
    # def test_dataframe_projection_parameterized(self, adaptee, degree, interaction_only):
    #     adaptee_kwargs = {'degree': degree, 'interaction_only': interaction_only}
    #     self._test_dataframe_projection(adaptee, adaptee_kwargs, num_random_points=10)

    def _test_dataframe_projection(self, adaptee, adapter_kwargs, num_random_points):
        num_adaptee_continuous_dims = 0
        for adaptee_dim in adaptee.dimensions:
            if isinstance(adaptee_dim, ContinuousDimension):
                num_adaptee_continuous_dims += 1

        # count the number of polynomial terms expected excluding the constant term
        if adapter_kwargs['interaction_only']:
            num_target_continuous_dims_expected = 0
            for i in range(adapter_kwargs['degree']):
                num_target_continuous_dims_expected += self.n_choose_k(num_adaptee_continuous_dims, i+1)
        else:
            num_target_continuous_dims_expected = self.n_choose_k(adapter_kwargs['degree'] + num_adaptee_continuous_dims, num_adaptee_continuous_dims) - 1

        adapter = ContinuousToPolynomialBasisHypergridAdapter(adaptee=adaptee, **adapter_kwargs)
        num_polynomial_features = len(adapter.get_column_names_for_polynomial_features())
        assert num_polynomial_features == num_target_continuous_dims_expected

        original_df = adaptee.random_dataframe(num_samples=num_random_points)

        # test in_place=False
        projected_df = adapter.project_dataframe(df=original_df, in_place=False)
        assert id(original_df) != id(projected_df)
        assert all([target_dim_name in projected_df.columns.values for target_dim_name in adapter.get_column_names_for_polynomial_features()])

        # test values are as expected
        self._test_polynomial_feature_values_are_as_expected(adapter, projected_df)

        unprojected_df = adapter.unproject_dataframe(df=projected_df, in_place=False)
        # since NaNs can not be passed through sklearn's PolynomialFeatures transform(), they are replaced w/ 0s during projection
        # hence the unprojected data frame will have 0s where the original had NaNs.
        original_df_with_fillna_zeros = original_df.fillna(0)
        assert original_df_with_fillna_zeros.equals(unprojected_df)

        # test in_place=True
        projected_in_place_df = adapter.project_dataframe(original_df, in_place=True)
        assert id(original_df) == id(projected_in_place_df)
        assert projected_in_place_df.equals(projected_df)
        assert all([target_dim_name in projected_in_place_df.columns.values for target_dim_name in
                    adapter.get_column_names_for_polynomial_features()])

        # test values are as expected
        self._test_polynomial_feature_values_are_as_expected(adapter, projected_in_place_df)

        unprojected_in_place_df = adapter.unproject_dataframe(df=projected_in_place_df, in_place=True)
        assert original_df_with_fillna_zeros.equals(unprojected_in_place_df)

    @staticmethod
    def _test_point_projection(adaptee, adapter_kwargs, num_random_points):
        adapter = ContinuousToPolynomialBasisHypergridAdapter(adaptee=adaptee, **adapter_kwargs)

        for _ in range(num_random_points):
            original_point = adaptee.random()
            projected_point = adapter.project_point(original_point)
            unprojected_point = adapter.unproject_point(projected_point)
            assert original_point == unprojected_point

    @staticmethod
    def _test_polynomial_feature_values_are_as_expected(adapter, projected_df):
        # Determine if target column values contain the expected polynomial feature values
        # This is done using the PolynomialFeatures powers_ table where the rows correspond to the target features
        # and the columns to the adaptee dimensions being transformed
        target_dim_names = adapter.get_column_names_for_polynomial_features()
        for i, ith_target_dim_powers in enumerate(adapter.get_polynomial_feature_powers_table()):
            # only testing higher degree monomials since the adaptee continuous dimensions are not altered
            if ith_target_dim_powers.sum() <= 1:
                continue
            target_dim_name = target_dim_names[i]
            observed_values = projected_df[target_dim_name].to_numpy().reshape(-1, 1)

            # construct expected ith target values
            expected_values = np.ones((len(projected_df.index.values), 1))
            for j, jth_adaptee_dim_power in enumerate(ith_target_dim_powers):
                if jth_adaptee_dim_power == 0:
                    continue
                jth_dim_name = target_dim_names[j]
                input_values = projected_df[jth_dim_name].to_numpy().reshape(-1, 1)
                expected_values = expected_values * (input_values ** jth_adaptee_dim_power)

            epsilon = 10 ** -9
            sum_diffs = np.abs(expected_values - observed_values).sum()
            if sum_diffs >= epsilon:
                print('expected: ', expected_values)
                print('observed: ', observed_values)
            assert sum_diffs < epsilon
