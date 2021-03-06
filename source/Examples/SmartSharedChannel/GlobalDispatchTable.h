//*********************************************************************
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root
// for license information.
//
// @File: GlobalDispatchTable.h
//
// Purpose:
//      <description>
//
// Notes:
//      <special-instructions>
//
//*********************************************************************

#pragma once

// Include SmartSharedChannel codegen files.
//
#include "SmartSharedChannel/SettingsProvider_gen_base.h"
#include "SmartSharedChannel/SettingsProvider_gen_callbacks.h"
#include "SmartSharedChannel/SettingsProvider_gen_dispatch.h"

// Include Mlos.UnitTest codegen files.
//
#include "Mlos.UnitTest/SettingsProvider_gen_base.h"
#include "Mlos.UnitTest/SettingsProvider_gen_callbacks.h"
#include "Mlos.UnitTest/SettingsProvider_gen_dispatch.h"

// Base indexes for all included dispatch tables.
//
constexpr uint32_t Mlos::UnitTest::ObjectDeserializationHandler::DispatchTableBaseIndex()
{
    return static_cast<uint32_t>(Mlos::Core::ObjectDeserializationHandler::DispatchTableElementCount());
}

constexpr uint32_t SmartSharedChannel::ObjectDeserializationHandler::DispatchTableBaseIndex()
{
    return static_cast<uint32_t>(Mlos::UnitTest::ObjectDeserializationHandler::DispatchTableBaseIndex() +
        Mlos::UnitTest::ObjectDeserializationHandler::DispatchTableElementCount());
}

constexpr auto GlobalDispatchTable()
{
    auto globalDispatchTable = Mlos::Core::DispatchTable<0>()
        .concatenate(Mlos::Core::ObjectDeserializationHandler::DispatchTable)
        .concatenate(Mlos::UnitTest::ObjectDeserializationHandler::DispatchTable)
        .concatenate(SmartSharedChannel::ObjectDeserializationHandler::DispatchTable);

    return globalDispatchTable;
}
