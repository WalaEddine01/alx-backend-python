# Core Testing Concepts Mind Map

## Interactive Canvas (JSON)
Paste this into a `.canvas` file in Obsidian:
```json
{
  "nodes": [
    {
      "id": "core",
      "type": "text",
      "text": "# Core Testing Concepts",
      "font": { "size": 24 },
      "x": 0,
      "y": -360,
      "width": 290,
      "height": 125,
      "color": "1"
    },
    {
      "id": "unit",
      "type": "text",
      "text": "## Unit Testing",
      "x": -365,
      "y": -100,
      "width": 220,
      "height": 50,
      "color": "2"
    },
    {
      "id": "unit-def",
      "type": "text",
      "text": "**Definition**: Tests individual components in isolation\n**Scope**: Single functions/methods/classes\n**Purpose**: Verify independent behavior",
      "x": -540,
      "y": 60,
      "width": 240,
      "height": 270
    },
    {
      "id": "unit-chars",
      "type": "text",
      "text": "**Characteristics**:\n- Fast execution\n- Minimal setup\n- Clear failure points\n- High code coverage",
      "x": -200,
      "y": 60,
      "width": 200,
      "height": 270
    },
    {
      "id": "integration",
      "type": "text",
      "text": "## Integration Testing",
      "x": 435,
      "y": -125,
      "width": 220,
      "height": 75,
      "color": "3"
    },
    {
      "id": "int-def",
      "type": "text",
      "text": "**Definition**: Tests component interactions\n**Scope**: Multiple units\n**Purpose**: Ensure system coherence",
      "x": 200,
      "y": 60,
      "width": 200,
      "height": 220
    },
    {
      "id": "int-chars",
      "type": "text",
      "text": "**Characteristics**:\n- Tests real dependencies\n- Slower than unit tests\n- Reveals integration issues\n- Closer to production",
      "x": 655,
      "y": 65,
      "width": 200,
      "height": 315
    },
    {
      "id": "deps",
      "type": "text",
      "text": "## Dependencies & Mocking",
      "x": -610,
      "y": 375,
      "width": 240,
      "height": 100,
      "color": "4"
    },
    {
      "id": "dep-types",
      "type": "text",
      "text": "**Types of Dependencies**:\n- **External**:\n  - APIs\n  - Databases\n  - Files\n  - Libraries\n- **Internal**:\n  - Other classes\n  - Configs\n  - Cache\n  - Logging",
      "x": -970,
      "y": 600,
      "width": 320,
      "height": 350
    },
    {
      "id": "mocks",
      "type": "text",
      "text": "**Mock Objects**:\n- Simulate real dependencies\n- **Purpose**:\n  - Isolate tests\n  - Control behavior\n  - Avoid externals\n  - Reduce complexity",
      "x": -610,
      "y": 600,
      "width": 270,
      "height": 420
    },
    {
      "id": "param",
      "type": "text",
      "text": "## Parameterized Testing",
      "x": 0,
      "y": 400,
      "width": 220,
      "height": 120,
      "color": "5"
    },
    {
      "id": "param-details",
      "type": "text",
      "text": "**Definition**: Tests with multiple inputs\n**Benefits**:\n- Less duplication\n- Easy maintenance\n- Better coverage\n- Clear cases",
      "x": -90,
      "y": 635,
      "width": 310,
      "height": 350
    },
    {
      "id": "memo",
      "type": "text",
      "text": "## Memoization",
      "x": 400,
      "y": 400,
      "width": 220,
      "height": 50,
      "color": "6"
    },
    {
      "id": "memo-details",
      "type": "text",
      "text": "**Definition**: Caching for optimization\n**Use Cases**:\n- Expensive calculations\n- Frequent calls\n- DB queries\n- API responses",
      "x": 420,
      "y": 635,
      "width": 200,
      "height": 315
    },
    {
      "id": "strategy",
      "type": "text",
      "text": "# Testing Strategy",
      "font": { "size": 24 },
      "x": 10,
      "y": 1140,
      "width": 335,
      "height": 90,
      "color": "7"
    },
    {
      "id": "unit-best",
      "type": "text",
      "text": "**Unit Test Best Practices**:\n- Keep tests independent\n- Meaningful assertions\n- Mock externals\n- Test errors\n- Fast execution",
      "x": -210,
      "y": 1335,
      "width": 200,
      "height": 300
    },
    {
      "id": "int-best",
      "type": "text",
      "text": "**Integration Test Best Practices**:\n- Focus on key workflows\n- Test real scenarios\n- Include error handling\n- Verify data consistency",
      "x": 410,
      "y": 1335,
      "width": 200,
      "height": 305
    },
    {
      "id": "8f9368ce0c5400c4",
      "type": "text",
      "text": "```mermaid\nflowchart TD\n    subgraph Core[\"Core Testing Concepts\"]\n        UT[Unit Tests]\n        IT[Integration Tests]\n    end\n    \n    subgraph Support[\"Supporting Tools\"]\n        MO[Mock Objects]\n        PT[Parameterized Testing]\n        ME[Memoization]\n    end\n    \n    subgraph Purpose[\"Primary Purpose\"]\n        UP[\"• Isolate Components<br/>• Test Individual Units<br/>• Fast Execution\"]\n        IP[\"• Verify Integration<br/>• Test System Flow<br/>• Real Dependencies\"]\n    end\n    \n    subgraph Benefits[\"Key Benefits\"]\n        UB[\"• Faster Execution<br/>• Clear Failures<br/>• Better Coverage\"]\n        IB[\"• Real Behavior<br/>• System Validation<br/>• Integration Checks\"]\n    end\n    \n    %% Connections\n    UT --> UP\n    IT --> IP\n    UT --> UB\n    IT --> IB\n    MO --> UT\n    PT --> UT & IT\n    ME --> UT & IT\n    \n    %% Styling\n    classDef core fill:#f9f,stroke:#333,stroke-width:2px\n    classDef support fill:#9ff,stroke:#333,stroke-width:2px\n    classDef purpose fill:#fff,stroke:#333,stroke-dasharray: 5 5\n    classDef benefits fill:#fff,stroke:#333,stroke-dasharray: 5 5\n    \n    class UT,IT core\n    class MO,PT,ME support\n    class UP,IP purpose\n    class UB,IB benefits\n```",
      "x": -2600,
      "y": 510,
      "width": 1270,
      "height": 530
    },
    {
      "id": "d40927764f71532a",
      "type": "file",
      "file": "Week04/Screenshot 2025-05-29 142829.png",
      "x": -2648,
      "y": -37,
      "width": 1366,
      "height": 462
    }
  ],
  "edges": [
    {
      "id": "92ac462b1c1a3f1f",
      "fromNode": "core",
      "fromSide": "left",
      "toNode": "unit",
      "toSide": "top"
    },
    {
      "id": "ad91492121486616",
      "fromNode": "core",
      "fromSide": "right",
      "toNode": "integration",
      "toSide": "top"
    },
    {
      "id": "d6c630c08fd2cbb3",
      "fromNode": "unit",
      "fromSide": "bottom",
      "toNode": "unit-def",
      "toSide": "top"
    },
    {
      "id": "daaa7b9ee7099bd8",
      "fromNode": "unit",
      "fromSide": "bottom",
      "toNode": "unit-chars",
      "toSide": "top"
    },
    {
      "id": "20c6abfba9bfd206",
      "fromNode": "integration",
      "fromSide": "bottom",
      "toNode": "int-def",
      "toSide": "top"
    },
    {
      "id": "caa64e6a9e1f30fc",
      "fromNode": "integration",
      "fromSide": "bottom",
      "toNode": "int-chars",
      "toSide": "top"
    },
    {
      "id": "5f449dae83093857",
      "fromNode": "deps",
      "fromSide": "bottom",
      "toNode": "dep-types",
      "toSide": "top"
    },
    {
      "id": "7873f4a3c2f471fc",
      "fromNode": "deps",
      "fromSide": "bottom",
      "toNode": "mocks",
      "toSide": "top"
    },
    {
      "id": "3ffc36e1270dfe31",
      "fromNode": "param",
      "fromSide": "bottom",
      "toNode": "param-details",
      "toSide": "top"
    },
    {
      "id": "ef9ace30099b5d79",
      "fromNode": "memo",
      "fromSide": "bottom",
      "toNode": "memo-details",
      "toSide": "top"
    },
    {
      "id": "a4c9dd3745497658",
      "fromNode": "strategy",
      "fromSide": "bottom",
      "toNode": "unit-best",
      "toSide": "top"
    },
    {
      "id": "a8a613d865fb265b",
      "fromNode": "strategy",
      "fromSide": "bottom",
      "toNode": "int-best",
      "toSide": "top"
    }
  ]
}